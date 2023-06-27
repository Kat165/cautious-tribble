namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class g3 : DbMigration
    {
        public override void Up()
        {
            DropForeignKey("dbo.Artiffacts", "Right_Id", "dbo.Rights");
            DropForeignKey("dbo.Classes", "Right_Id", "dbo.Rights");
            DropForeignKey("dbo.Users", "Right_Id", "dbo.Rights");
            DropIndex("dbo.Artiffacts", new[] { "Right_Id" });
            DropIndex("dbo.Classes", new[] { "Right_Id" });
            DropIndex("dbo.Users", new[] { "Right_Id" });
            AddColumn("dbo.Rights", "ClassesAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "ArtifactsAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "UsersAllowedToEdit", c => c.String());
            DropColumn("dbo.Artiffacts", "Right_Id");
            DropColumn("dbo.Classes", "Right_Id");
            DropColumn("dbo.Users", "Right_Id");
        }
        
        public override void Down()
        {
            AddColumn("dbo.Users", "Right_Id", c => c.Int());
            AddColumn("dbo.Classes", "Right_Id", c => c.Int());
            AddColumn("dbo.Artiffacts", "Right_Id", c => c.Int());
            DropColumn("dbo.Rights", "UsersAllowedToEdit");
            DropColumn("dbo.Rights", "ArtifactsAllowedToEdit");
            DropColumn("dbo.Rights", "ClassesAllowedToEdit");
            CreateIndex("dbo.Users", "Right_Id");
            CreateIndex("dbo.Classes", "Right_Id");
            CreateIndex("dbo.Artiffacts", "Right_Id");
            AddForeignKey("dbo.Users", "Right_Id", "dbo.Rights", "Id");
            AddForeignKey("dbo.Classes", "Right_Id", "dbo.Rights", "Id");
            AddForeignKey("dbo.Artiffacts", "Right_Id", "dbo.Rights", "Id");
        }
    }
}
