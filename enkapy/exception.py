class EnkaError(Exception):
    pass


class ValidateUIDError(EnkaError):
    pass


class UIDNotFounded(EnkaError):
    pass


class WrongUIDFormat(EnkaError):
    pass


class PlayerDoesNOTExist(EnkaError):
    pass


class GameMaintenance(EnkaError):
    pass


class RateLimited(EnkaError):
    pass


class GeneralServerError(EnkaError):
    pass
