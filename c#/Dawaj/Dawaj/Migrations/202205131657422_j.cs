namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class j : DbMigration
    {
        public override void Up()
        {
            AlterColumn("dbo.Classes", "mainAtribute", c => c.String());
        }
        
        public override void Down()
        {
            AlterColumn("dbo.Classes", "mainAtribute", c => c.Int(nullable: false));
        }
    }
}
