namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class h1 : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Artiffacts", "mainAtribute", c => c.Int(nullable: false));
        }
        
        public override void Down()
        {
            DropColumn("dbo.Artiffacts", "mainAtribute");
        }
    }
}
