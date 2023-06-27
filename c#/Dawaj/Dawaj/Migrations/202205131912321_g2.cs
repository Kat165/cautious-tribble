namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class g2 : DbMigration
    {
        public override void Up()
        {
            AlterColumn("dbo.Artiffacts", "UserId", c => c.Int(nullable: false));
        }
        
        public override void Down()
        {
            AlterColumn("dbo.Artiffacts", "UserId", c => c.String());
        }
    }
}
