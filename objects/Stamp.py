class MessageStamp:
    def __init__(self,userId,stampId,count,createdAt,updatedAt) -> None:
        self.userId = userId
        self.stampId = stampId
        self.count = count
        self.createdAt = createdAt
        self.updatedAt = updatedAt

class Stamp:
    def __init__(self,id,name,creatorId,createdAt,updatedAt,fileId,isUnicode):
        self.id = id
        self.name = name
        self.creatorId = creatorId
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.fileId = fileId
        self.isUnicode = isUnicode