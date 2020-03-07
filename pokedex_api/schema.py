from graphene import Schema, ObjectType, Field
from graphene_django.debug import DjangoDebug

# import pokedex.schema


class Query(
    # pokedex.schema.Query,
    ObjectType
):
    debug = Field(DjangoDebug, name='__debug')


class Mutation(
    # pokedex.schema.Mutation, 
    ObjectType
):
    debug = Field(DjangoDebug, name='__debug')


schema = Schema(
    query=Query,
    mutation=Mutation
)