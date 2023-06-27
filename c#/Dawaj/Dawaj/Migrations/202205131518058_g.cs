namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class g : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Atributes",
                c => new
                    {
                        Id = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        Value = c.String(),
                        Artiffact_Id = c.Int(),
                    })
                .PrimaryKey(t => t.Id)
                .ForeignKey("dbo.Artiffacts", t => t.Artiffact_Id)
                .Index(t => t.Artiffact_Id);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Atributes", "Artiffact_Id", "dbo.Artiffacts");
            DropIndex("dbo.Atributes", new[] { "Artiffact_Id" });
            DropTable("dbo.Atributes");
        }
    }
}
