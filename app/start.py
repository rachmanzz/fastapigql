from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp
from app.queries_schema import Query

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))