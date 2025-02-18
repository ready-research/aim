import click
from click import core

from aimcore.cli.init import commands as init_commands
from aimcore.cli.version import commands as version_commands
from aimcore.cli.ui import commands as ui_commands
from aimcore.cli.server import commands as server_commands
from aimcore.cli.telemetry import commands as telemetry_commands
from aimcore.cli.package import commands as package_commands
from aimcore.cli.conatiners import commands as container_commands
from aimcore.cli.migrate import commands as migrate_commands

core._verify_python3_env = lambda: None


@click.group()
def cli_entry_point():
    pass


cli_entry_point.add_command(init_commands.init)
cli_entry_point.add_command(version_commands.version)
cli_entry_point.add_command(ui_commands.ui)
cli_entry_point.add_command(ui_commands.up)
cli_entry_point.add_command(server_commands.server)
cli_entry_point.add_command(telemetry_commands.telemetry)
cli_entry_point.add_command(package_commands.packages)
cli_entry_point.add_command(package_commands.packages, name='apps')
cli_entry_point.add_command(container_commands.containers)
cli_entry_point.add_command(migrate_commands.migrate)
