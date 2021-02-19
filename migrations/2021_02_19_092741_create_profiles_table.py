from orator.migrations import Migration


class CreateProfilesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profiles') as table:
            table.big_increments('id')
            table.string('name')
            table.string('phone').nullable()
            table.string('address').nullable()
            table.string('city', 50).nullable()
            table.string('state', 50).nullable()
            table.string('country', 50).nullable()
            table.big_integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profiles')
