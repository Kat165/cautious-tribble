namespace Dawaj.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class df : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Rights", "ClassesAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "ArtifactsAllowedToEdit", c => c.String());
            AddColumn("dbo.Rights", "UsersAllowedToEdit", c => c.String());
        }
        
        public override void Down()
        {
            DropColumn("dbo.Rights", "UsersAllowedToEdit");
            DropColumn("dbo.Rights", "ArtifactsAllowedToEdit");
            DropColumn("dbo.Rights", "ClassesAllowedToEdit");
        }
    }
}
