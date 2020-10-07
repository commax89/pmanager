class Cli:

    @staticmethod
    def execute(context, config):
        if context.invoked_subcommand and context.invoked_subcommand == 'setup':
            return

        project_path = config.get_project_path()
        if not project_path:
            context.fail("There is no setup yet. Please run 'pmanager setup'")
