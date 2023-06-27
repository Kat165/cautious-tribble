namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class g1 : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Artiffacts", "Class", c => c.String());
        }
        
        public override void Down()
        {
            DropColumn("dbo.Artiffacts", "Class");
        }
    }
}
