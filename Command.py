from _future_ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    
    def _init_(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Lihat, saya bisa melakukan hal-hal sederhana seperti mencetak"
              f"({self._payload})")


class ComplexCommand(Command):

    def _init_(self, receiver: Receiver, a: str, b: str) -> None:

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:

        print("ComplexCommand: Hal-hal kompleks harus dilakukan oleh objek penerima", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:

        print("Invoker: Apakah ada yang ingin sesuatu dilakukan sebelum saya mulai?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...melakukan sesuatu yang sangat penting...")

        print("Invoker: Apakah ada yang ingin sesuatu dilakukan setelah saya selesai?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if _name_ == "_main_":

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()