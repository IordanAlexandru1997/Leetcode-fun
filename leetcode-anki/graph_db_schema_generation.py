import json
import random
import string
import time
from tkinter import *
from tkinter import ttk
from neo4j import GraphDatabase


class Neo4jSchemaGenerator:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_schema(self, schema_str):
        schema = json.loads(schema_str)

        with self.driver.session() as session:
            for node in schema["nodes"]:
                label = node["label"]
                for prop in node["properties"]:
                    session.write_transaction(self.create_node_constraint, label, prop)

    @staticmethod
    def create_node_constraint(tx, label, property_key):
        query = f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{label}) REQUIRE n.{property_key} IS UNIQUE"
        tx.run(query)

    @staticmethod
    def create_relationship_constraint(tx, relationship):
        start_node = relationship["start_node"]
        end_node = relationship["end_node"]
        rel_type = relationship["type"]

        for property in relationship["properties"]:
            query = f"CREATE CONSTRAINT ON ()-[r:{rel_type}]->() ASSERT r.{property} IS UNIQUE"
            tx.run(query)

    def insert_random_data(self, schema_str, num_records):
        schema = json.loads(schema_str)

        with self.driver.session() as session:
            for _ in range(num_records):
                for node in schema["nodes"]:
                    session.write_transaction(
                        self.create_random_node, node["label"], node["properties"]
                    )

                for relationship in schema["relationships"]:
                    start_node_label = relationship["start_node"]
                    end_node_label = relationship["end_node"]
                    relationship_type = relationship["type"]

                    start_node_props = None
                    end_node_props = None
                    for node in schema["nodes"]:
                        if node["label"] == start_node_label:
                            start_node_props = node["properties"]
                        if node["label"] == end_node_label:
                            end_node_props = node["properties"]

                    session.write_transaction(
                        self.create_random_relationship,
                        start_node_label,
                        end_node_label,
                        relationship_type,
                        start_node_props,
                        end_node_props,
                    )

    @staticmethod
    def random_string(length):
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    @staticmethod
    def random_value():
        value_type = random.choice(["int", "float", "string"])
        if value_type == "int":
            return random.randint(1, 100)
        elif value_type == "float":
            return round(random.uniform(1, 100), 2)
        elif value_type == "string":
            return Neo4jSchemaGenerator.random_string(random.randint(3, 15))

    @staticmethod
    def create_random_node(tx, label, properties):
        property_values = {}
        for property in properties:
            value = Neo4jSchemaGenerator.random_value()
            property_values[property] = value

        # Check for duplicates
        existing_node = tx.run(
            f"""MATCH (n:{label}) WHERE {' AND '.join([f'n.{k} = "{v}"' for k, v in property_values.items()])} RETURN n"""
        ).single()

        if existing_node is not None:
            return

        query = (
            "CREATE (n:"
            + label
            + " {"
            + ", ".join([f'{k}: "{v}"' for k, v in property_values.items()])
            + "})"
        )
        tx.run(query)

    def create_random_relationships(self, schema):
        with self.driver.session() as session:
            nodes = {}
            for node in schema["nodes"]:
                nodes[node["label"]] = list(node["properties"])

            for start_node_label in nodes.keys():
                for end_node_label in nodes.keys():
                    if start_node_label == end_node_label:
                        continue
                    for relationship in schema["relationships"]:
                        relationship_type = relationship["type"]
                        session.write_transaction(
                            self.create_random_relationship,
                            start_node_label,
                            end_node_label,
                            relationship_type,
                            nodes[start_node_label],
                            nodes[end_node_label],
                        )

    def create_random_relationship(
        self, tx, start_node, end_node, rel_type, label1_props, label2_props
    ):
        label1_props = label1_props or []
        label2_props = label2_props or []

        query = (
            f"MATCH (a:{start_node['label']}), (b:{end_node['label']})"
            f" WHERE id(a) < id(b)"
            f" CREATE (a)-[r:{rel_type}]->(b)"
            f""" SET r += {{ {', '.join([f'{k}: "{self.random_value()}"' for k in label1_props + label2_props])} }}"""
        )
        tx.run(query)

    def query_data(self, schema_str):
        schema = json.loads(schema_str)
        query_results = []

        with self.driver.session() as session:
            for node in schema["nodes"]:
                result = session.read_transaction(self.query_nodes, node["label"])
                query_results.append(result)

            for relationship in schema["relationships"]:
                result = session.read_transaction(
                    self.query_relationships, relationship
                )
                query_results.append(result)

        return query_results

    @staticmethod
    def query_nodes(tx, label):
        query = f"MATCH (n:{label}) RETURN n LIMIT 10"
        result = tx.run(query)
        return list(result)

    @staticmethod
    def query_relationships(tx, relationship):
        start_node = relationship["start_node"]
        end_node = relationship["end_node"]
        rel_type = relationship["type"]

        properties = start_node.get("properties", [])  # get the list of properties
        prop_str = ", ".join(
            [f"{k}: '{v}'" for k, v in zip(properties, start_node.get("values", []))]
        )  # use zip to iterate over properties and values together

        query = f"MATCH (a:{start_node['label']} {{{prop_str}}}), (b:{end_node['label']}) WHERE EXISTS((a)-[:{rel_type}]->(b)) RETURN a, b"
        result = tx.run(query)
        return list(result)


def create_schema():
    schema_str = schema_input.get("1.0", "end-1c")
    neo4j.create_schema(schema_str)


def insert_random_data(num_records):
    schema_str = schema_input.get("1.0", "end-1c")
    start_time = time.time()
    neo4j.insert_random_data(schema_str, num_records)
    end_time = time.time()

    log.insert(
        INSERT,
        f"Inserted {num_records} random data in {end_time - start_time:.2f} seconds\n",
    )


def query_data():
    schema_str = schema_input.get("1.0", "end-1c")
    start_time = time.time()
    results = neo4j.query_data(schema_str)
    end_time = time.time()

    for result in results:
        log.insert(INSERT, f"Query result: {result}\n")

    log.insert(INSERT, f"Queried data in {end_time - start_time:.2f} seconds\n")


neo4j = Neo4jSchemaGenerator("bolt://localhost:7687", "neo4j", "password")

root = Tk()
root.title("Neo4j Schema Generator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(N, W, E, S))

schema_input = Text(frame, width=80, height=10)
schema_input.grid(column=0, row=0, columnspan=3)

create_schema_button = ttk.Button(frame, text="Create Schema", command=create_schema)
create_schema_button.grid(column=0, row=1)

random_data_buttons = [
    ttk.Button(
        frame, text=f"{num} Records", command=lambda num=num: insert_random_data(num)
    )
    for num in [10, 100, 1000]
]
for i, button in enumerate(random_data_buttons):
    button.grid(column=i, row=2)

query_data_button = ttk.Button(frame, text="Query Data", command=query_data)
query_data_button.grid(column=2, row=3)

log = Text(frame, width=80, height=10)
log.grid(column=0, row=4, columnspan=3)

root.mainloop()

neo4j.close()
