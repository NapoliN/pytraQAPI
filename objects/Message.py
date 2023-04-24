from .Stamp import MessageStamp

class Message:
    def __init__(self,id,userId,channelId,content,createdAt,updatedAt,pinned,stamps,threadId) -> None:
        self.id = id
        self.userId = userId,
        self.channelId = channelId
        self.content = content
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.pinned = pinned
        self.stamps = [MessageStamp(**o) for o in stamps]
        self.theadId = threadId