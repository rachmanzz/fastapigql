from fastapi import FastAPI, Request, Depends
import graphene
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.datastructures import URL

from app.schema import Query
from app.mutator import Mutation

app = FastAPI()

schema = graphene.Schema(
    query=Query,
    mutation=Mutation)

graphql_app = GraphQLApp(
    schema=schema,
    executor_class=AsyncioExecutor)

# app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/graphql')
async def graphql(request: Request):
    request._url = URL('/graphql')
    return await graphql_app.handle_graphql(request=request)

@app.post('/graphql')
async def graphql(request: Request):
    return await graphql_app.handle_graphql(request=request)