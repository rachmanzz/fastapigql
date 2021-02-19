from orator.migrations import Migration


class CreateAccountsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('accounts') as table:
            table.big_increments('id')
            table.double('balance').default(0.0)
            table.enum('type', ['personal','business'])
            table.big_integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('accounts')
