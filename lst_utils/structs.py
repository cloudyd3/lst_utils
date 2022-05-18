import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Dispute:
    date: str = dataclasses.field(default_factory=lambda: datetime.now().strftime("%d.%m.%Y %H.%M"))
    playerName: str = dataclasses.field(default_factory=lambda: "")
    order: str = dataclasses.field(default_factory=lambda: "")
    playerStatus: str = dataclasses.field(default_factory=lambda: "")
    game: str = dataclasses.field(default_factory=lambda: "")
    violation: str = dataclasses.field(default_factory=lambda: "")
    punishment: str = dataclasses.field(default_factory=lambda: "")
    comment: str = dataclasses.field(default_factory=lambda: "")