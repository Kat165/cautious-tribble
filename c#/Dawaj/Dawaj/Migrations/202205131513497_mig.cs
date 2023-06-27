namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class mig : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Artiffacts", "UserId", c => c.String());
            AddColumn("dbo.Artiffacts", "Atributes", c => c.String());
            DropColumn("dbo.Artiffacts", "Nos");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Artiffacts", "Nos", c => c.String());
            DropColumn("dbo.Artiffacts", "Atributes");
            DropColumn("dbo.Artiffacts", "UserId");
        }
    }
}
