from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.big_increments('id')
            table.string('username', 50).unique().nullable()
            table.string('email', 100).unique()
            table.string('password').nullable()
            table.enum('status', ['guest','partner','admin'])
            table.boolean('is_active').default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
