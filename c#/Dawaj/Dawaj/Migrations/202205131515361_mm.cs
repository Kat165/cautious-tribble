namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class mm : DbMigration
    {
        public override void Up()
        {
            DropColumn("dbo.Artiffacts", "Atributes");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Artiffacts", "Atributes", c => c.String());
        }
    }
}
