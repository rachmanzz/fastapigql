from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

from app.schema import Query
from app.mutator import Mutation

app = FastAPI()


app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))