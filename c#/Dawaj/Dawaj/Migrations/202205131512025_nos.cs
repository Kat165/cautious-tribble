namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class nos : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Artiffacts", "Nos", c => c.String());
            DropColumn("dbo.Artiffacts", "UserId");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Artiffacts", "UserId", c => c.String());
            DropColumn("dbo.Artiffacts", "Nos");
        }
    }
}
