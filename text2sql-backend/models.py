from typing import Literal, Union

from pydantic.dataclasses import dataclass

ResultType = Union[Literal["sql"], Literal["code"]]


@dataclass
class Result:
    result_id: int
    type: ResultType
    content: str


@dataclass
class UnsavedResult:
    type: ResultType
    content: str


@dataclass
class MessageWithResults:
    content: str
    role: str
    results: list[Result]
    message_id: int


@dataclass
class Conversation:
    conversation_id: str
    session_id: str
    name: str


@dataclass
class Session:
    name: str
    database: str
    session_id: str
    dsn: str
    dialect: str


class ConversationWithMessagesWithResults(Conversation):
    messages: list[MessageWithResults]