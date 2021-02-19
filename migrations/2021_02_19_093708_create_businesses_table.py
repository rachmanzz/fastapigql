from orator.migrations import Migration


class CreateBusinessesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('businesses') as table:
            table.increments('id')
            table.string('key')
            table.big_integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('businesses')
