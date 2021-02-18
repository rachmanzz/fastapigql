from fastapi import FastAPI
import graphene

from starlette.graphql import GraphQLApp

from app.resources.User import Query as UserQuery
app = FastAPI()

app.add_route('/auth/graphql', GraphQLApp(schema=graphene.Schema(query=UserQuery)))