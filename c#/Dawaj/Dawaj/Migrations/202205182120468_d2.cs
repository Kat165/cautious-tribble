namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class d2 : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Artiffacts", "Right_Id", c => c.Int());
            AddColumn("dbo.Classes", "Right_Id", c => c.Int());
            AddColumn("dbo.Users", "Right_Id", c => c.Int());
            CreateIndex("dbo.Artiffacts", "Right_Id");
            CreateIndex("dbo.Classes", "Right_Id");
            CreateIndex("dbo.Users", "Right_Id");
            AddForeignKey("dbo.Artiffacts", "Right_Id", "dbo.Rights", "Id");
            AddForeignKey("dbo.Classes", "Right_Id", "dbo.Rights", "Id");
            AddForeignKey("dbo.Users", "Right_Id", "dbo.Rights", "Id");
            DropColumn("dbo.Rights", "ClassesAllowedToEdit");
            DropColumn("dbo.Rights", "ArtifactsAllowedToEdit");
            DropColumn("dbo.Rights", "UsersAllowedToEdit");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Rights", "UsersAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "ArtifactsAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "ClassesAllowedToEdit", c => c.String());
            DropForeignKey("dbo.Users", "Right_Id", "dbo.Rights");
            DropForeignKey("dbo.Classes", "Right_Id", "dbo.Rights");
            DropForeignKey("dbo.Artiffacts", "Right_Id", "dbo.Rights");
            DropIndex("dbo.Users", new[] { "Right_Id" });
            DropIndex("dbo.Classes", new[] { "Right_Id" });
            DropIndex("dbo.Artiffacts", new[] { "Right_Id" });
            DropColumn("dbo.Users", "Right_Id");
            DropColumn("dbo.Classes", "Right_Id");
            DropColumn("dbo.Artiffacts", "Right_Id");
        }
    }
}
