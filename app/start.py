from fastapi import FastAPI, Request, Depends
import graphene
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.datastructures import URL
from fastapi.middleware.cors import CORSMiddleware

from app.schema import Query
from app.mutator import Mutation
from app.Auth import AuthBase
from vendor.auth import get_current_user
from typing import Optional

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = graphene.Schema(
    query=Query,
    mutation=Mutation)

graphql_app = GraphQLApp(schema=schema, executor_class=AsyncioExecutor)

# app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/graphql')
async def graphql(request: Request):
    request._url = URL('/graphql')
    return await graphql_app.handle_graphql(request=request)

@app.post('/graphql')
async def graphql(request: Request, current_user: AuthBase = Depends(get_current_user)):
    request.state.current_user = current_user
    return await graphql_app.handle_graphql(request=request)