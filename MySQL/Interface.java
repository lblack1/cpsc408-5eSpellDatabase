// Interface for part 3 project - Lloyd Black
import java.sql.*;
import java.util.Scanner;

public class Interface {

	static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
	static final String DB_URL = "jdbc:mysql://localhost/sys?serverTimezone=UTC";

	// Database creds
	static final String USER = "root";
	static final String PASS = "[PASSWORD]";

	static final Scanner in = new Scanner(System.in);

	private static int GenerateID(Connection conn, String table) throws SQLException {

		String sql = "SELECT " + table.toLowerCase() + "ID FROM `" + table + "` ORDER BY " + table.toLowerCase() + "ID ASC";
		Statement stmt = conn.createStatement();
		ResultSet rs = stmt.executeQuery(sql);

		int id = 1;
		while (rs.next()) {
			if (id == rs.getInt(1)) {
				id++;
			} else {
				break;
			}
		}

		stmt.close();
		rs.close();

		return id;

	}

	private static String get(String prompt) {
		System.out.print(prompt);
		return in.nextLine();
	}

	private static int Insert(Connection conn) throws SQLException {


		System.out.println("\nInsert into which table?\n");
		System.out.println("\t1) Spell");
		System.out.println("\t2) Class");
		System.out.println("\t3) Usage");
		System.out.println("\t4) Effect");
		System.out.println("\t5) Class-Spell");
		System.out.println("\t6) Background");
		System.out.println("\t7) Character");

		int choice = Integer.parseInt(get(">>> "));

		String sql;
		PreparedStatement pstmt;

		switch (choice) {
			
			case 1:

				sql = "INSERT INTO Spell VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Spell"));
				pstmt.setString(2,get("Enter name: "));
				pstmt.setLong(3,Integer.parseInt(get("Enter level (0-9): ")));
				pstmt.setString(4,get("Enter school: "));
				pstmt.setString(5,get("Enter casting time: "));
				pstmt.setLong(6,Integer.parseInt(get("Enter range (-1 or higher): ")));
				pstmt.setString(7,get("Enter intended target description: "));
				pstmt.setLong(8,Integer.parseInt(get("Spell has Verbal component (0 for no, 1 for yes): ")));
				pstmt.setLong(9,Integer.parseInt(get("Spell has Somatic component (0 for no, 1 for yes): ")));
				pstmt.setString(10,get("Enter material components: "));
				pstmt.setLong(11,Integer.parseInt(get("Spell is concentration (0 for no, 1 for yes): ")));
				pstmt.setLong(12,Integer.parseInt(get("Enter duration (-1 or higher): ")));
				pstmt.setLong(13,Integer.parseInt(get("Enter ID of primary effect: ")));
				pstmt.setLong(14,Integer.parseInt(get("Enter ID of secondary effect: ")));

				return pstmt.executeUpdate();

			case 2:

				sql = "INSERT INTO Class VALUES (?,?,?,?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Class"));
				pstmt.setString(2,get("Enter class name: "));
				pstmt.setString(3,get("Enter class casting modifier: "));
				pstmt.setLong(4,Integer.parseInt(get("Class is half caster (0 for no, 1 for yes): ")));
				pstmt.setString(5,get("Enter class hit die: "));

				return pstmt.executeUpdate();

			case 3:

				sql = "INSERT INTO `Usage` VALUES (?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Usage"));
				pstmt.setString(2,get("Enter usage name: "));

				return pstmt.executeUpdate();

			case 4:

				sql = "INSERT INTO Effect VALUES (?,?,?,?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Effect"));
				pstmt.setLong(2,Integer.parseInt(get("Enter ID of parent usage: ")));
				pstmt.setString(3,get("Enter effect save: "));
				pstmt.setString(4,get("Enter effect damage: "));
				pstmt.setString(5,get("Enter additional effect text: "));

				return pstmt.executeUpdate();

			case 5:

				sql = "INSERT INTO ClassSpell VALUES (?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter Class ID: ")));
				pstmt.setLong(2,Integer.parseInt(get("Enter Spell ID: ")));

				return pstmt.executeUpdate();

			case 6: 

				sql = "INSERT INTO Background VALUES (?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Background"));
				pstmt.setString(2,get("Enter background name: "));

				return pstmt.executeUpdate();

			case 7:

				sql = "INSERT INTO `Character` VALUES (?,?,?,?,?,?,?,?,?,?,?)";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,GenerateID(conn, "Character"));
				pstmt.setString(2,get("Enter Character name: "));
				pstmt.setLong(3,Integer.parseInt(get("Enter background ID: ")));
				pstmt.setLong(4,Integer.parseInt(get("Enter first class ID: ")));
				pstmt.setLong(5,Integer.parseInt(get("Enter first level: ")));
				pstmt.setLong(6,Integer.parseInt(get("Enter second class ID: ")));
				pstmt.setLong(7,Integer.parseInt(get("Enter second level: ")));
				pstmt.setLong(8,Integer.parseInt(get("Enter third class ID: ")));
				pstmt.setLong(9,Integer.parseInt(get("Enter third level: ")));
				pstmt.setLong(10,Integer.parseInt(get("Enter fourth class ID: ")));
				pstmt.setLong(11,Integer.parseInt(get("Enter fourth level: ")));

				return pstmt.executeUpdate();

			default:

				System.out.println("Invalid option.");
				return 0;


		}

	}

	private static int Delete(Connection conn) throws SQLException {

		System.out.println("\nDelete from which table?\n");
		System.out.println("\t1) Spell");
		System.out.println("\t2) Class");
		System.out.println("\t3) Usage");
		System.out.println("\t4) Effect");
		System.out.println("\t5) Class-Spell");
		System.out.println("\t6) Background");
		System.out.println("\t7) Character");

		int choice = Integer.parseInt(get(">>> "));

		String sql;
		PreparedStatement pstmt;

		switch (choice) {

			case 1:

				sql = "DELETE FROM Spell WHERE spellID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Spell to delete: ")));

				return pstmt.executeUpdate();

			case 2:

				sql = "DELETE FROM Class WHERE classID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Class to delete: ")));

				return pstmt.executeUpdate();

			case 3:

				sql = "DELETE FROM `Usage` WHERE usageID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Usage to delete: ")));

				return pstmt.executeUpdate();
		
			case 4:

				sql = "DELETE FROM Effect WHERE effectID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Effect to delete: ")));

				return pstmt.executeUpdate();

			case 5:

				sql = "DELETE FROM ClassSpell WHERE classID=? AND spellID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of class relationship to delete: ")));
				pstmt.setLong(2,Integer.parseInt(get("Enter ID of spell relationship to delete: ")));

				return pstmt.executeUpdate();

			case 6:

				sql = "DELETE FROM Background WHERE backgroundID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Background to delete: ")));

				return pstmt.executeUpdate();

			case 7:

				sql = "DELETE FROM `Character` WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);

				pstmt.setLong(1,Integer.parseInt(get("Enter ID of Character to delete: ")));

				return pstmt.executeUpdate();

			default:

				System.out.println("Invalid option.");
				return 0;

		}

	}

	private static int Update(Connection conn) throws SQLException {

		String sql;
		PreparedStatement pstmt;

		int id = Integer.parseInt(get("\nEnter ID of character to update: "));

		System.out.println("Which column to update?");
		System.out.println("\t1) Name");
		System.out.println("\t2) Background");
		System.out.println("\t3) Class");
		System.out.println("\t4) Level");
		System.out.println("\t5) Second Class");
		System.out.println("\t6) Second Level");
		System.out.println("\t7) Third Class");
		System.out.println("\t8) Third Level");
		System.out.println("\t9) Fourth Class");
		System.out.println("\t10) Fourth Level");

		int choice = Integer.parseInt(get(">>> "));

		switch (choice) {

			case 1:
				sql = "UPDATE `Character` SET name=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1,get("Enter new name: "));
				break;
			case 2:
				sql = "UPDATE `Character` SET background=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter ID of new background: ")));
				break;
			case 3:
				sql = "UPDATE `Character` SET class=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter ID of new class: ")));
				break;
			case 4:
				sql = "UPDATE `Character` SET level=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter new level: ")));
				break;
			case 5:
				sql = "UPDATE `Character` SET secondClass=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter ID of new class: ")));
				break;
			case 6:
				sql = "UPDATE `Character` SET secondLevel=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter new level: ")));
				break;
			case 7:
				sql = "UPDATE `Character` SET thirdClass=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter ID of new class: ")));
				break;
			case 8:
				sql = "UPDATE `Character` SET thirdLevel=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter new level: ")));
				break;
			case 9:
				sql = "UPDATE `Character` SET fourthClass=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter ID of new class: ")));
				break;
			case 10:
				sql = "UPDATE `Character` SET fourthLevel=? WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter new level: ")));
				break;
			default:
				System.out.println("Invalid option.");
				return 0;

		}

		pstmt.setLong(2,id);
		return pstmt.executeUpdate();

	}

	private static int Query(Connection conn) throws SQLException {

		System.out.println("\nWhich query?\n");
		System.out.println("\t1) All spells linked to a given class");
		System.out.println("\t2) All spells available to a given character (grouped by class)");
		System.out.println("\t3) All child effects of a given usage");
		System.out.println("\t4) All characters that have access to a given spell");
		System.out.println("\t5) All info of a given spell");
		System.out.println("\t6) All info of a given character");
		System.out.println("\t7) All characters with at least one level in a given class");
		System.out.println("\t8) Number of spells with a given usage, grouped by school");
		System.out.println("\t9) Count of characters of a given level or higher, grouped by level");


		int choice = Integer.parseInt(get(">>> "));

		ResultSet rs;
		PreparedStatement pstmt;

		String sql;

		switch (choice) {

			case 1:
				sql = "SELECT Spell.spellID, Spell.name FROM Class NATURAL JOIN ClassSpell INNER JOIN Spell ON ClassSpell.spellID = Spell.spellID WHERE Class.classID=? ORDER BY Spell.spellID ASC";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter class ID for which to retrieve spells: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("ID: " + rs.getInt(1) + "; Name: " + rs.getString(2));
				}
				rs.close();
				return 1;

			case 2:
				sql = "SELECT Class.name, group_concat(' ID: ', Spell.spellID, '; Name: ', Spell.name) FROM Class NATURAL JOIN ClassSpell INNER JOIN Spell ON ClassSpell.spellID=Spell.spellID WHERE Class.classID=? GROUP BY Class.name";
				pstmt = conn.prepareStatement(sql);
				
				PreparedStatement pstmt2 = conn.prepareStatement("SELECT class, secondClass, thirdClass, fourthClass FROM `Character` WHERE characterID=?");
				pstmt2.setLong(1,Integer.parseInt(get("Enter character ID for which to retrieve spells: ")));
				ResultSet classes = pstmt2.executeQuery();

				int col = 1;
				classes.next();
				while (col<=4) {
					pstmt.setLong(1, classes.getInt(col++));
					rs = pstmt.executeQuery();
					while (rs.next()) {
						System.out.println();
						System.out.println("Class: " + rs.getString(1) + "; Spells: //" + rs.getString(2) + "//");
					}
					rs.close();
				}
				classes.close();
				return 1;

			case 3: 
				sql = "SELECT effectID, save, damage, txt FROM `Usage` NATURAL JOIN Effect WHERE usageID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter usage ID for which to retrieve effects: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("ID: " + rs.getInt(1) + "; Save: " + rs.getString(2) + "; Damage: " + rs.getString(3) + "; Text: " + rs.getString(4));
				}
				rs.close();
				return 1;

			case 4:
				sql = "SELECT classID FROM Spell NATURAL JOIN ClassSpell WHERE Spell.spellID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter spell ID for which to retrieve characters: ")));
				rs = pstmt.executeQuery();

				PreparedStatement pstmt3 = conn.prepareStatement("SELECT characterID, name FROM `Character` WHERE class=? OR secondClass=? OR thirdClass=? OR fourthClass=?");

				System.out.println();
				while (rs.next()) {
					pstmt3.setLong(1,rs.getInt(1));
					pstmt3.setLong(2,rs.getInt(1));
					pstmt3.setLong(3,rs.getInt(1));
					pstmt3.setLong(4,rs.getInt(1));
					ResultSet characters = pstmt3.executeQuery();
					while (characters.next()) {
						System.out.println("ID: " + characters.getInt(1) + "; Name: " + characters.getString(2));
					}
					characters.close();
				}
				rs.close();
				return 1;

			case 5:
				sql = "SELECT * FROM Spell WHERE spellID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter spell ID for which to retrieve info: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("Name: " + rs.getString(2));
					System.out.println("Level: " + rs.getInt(3));
					System.out.println("School: " + rs.getString(4));
					System.out.println("Casting Time: " + rs.getString(5));
					System.out.println("Range: " + rs.getInt(6));
					System.out.println("Target: " + rs.getString(7));
					System.out.println("Has Verbal Component: " + rs.getInt(8));
					System.out.println("Has Somatic Component: " + rs.getInt(9));
					System.out.println("Material Components: " + rs.getString(10));
					System.out.println("Is Concentration: " + rs.getInt(11));
					System.out.println("Duration: " + rs.getInt(12));
					System.out.println("Primary Effect: " + rs.getInt(13));
					System.out.println("Secondary Effect: " + rs.getInt(14));
				}
				rs.close();
				return 1;

			
			case 6:
				sql = "SELECT * FROM `Character` WHERE characterID=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter Character ID for which to retrieve info: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("Name: " + rs.getString(2));
					System.out.println("Background: " + rs.getInt(3));
					System.out.println("Class: " + rs.getInt(4));
					System.out.println("Level: " + rs.getInt(5));
					System.out.println("Second Class: " + rs.getInt(6));
					System.out.println("Second Level: " + rs.getInt(7));
					System.out.println("Third Class: " + rs.getInt(8));
					System.out.println("Third Level: " + rs.getInt(9));
					System.out.println("Fourth Class: " + rs.getInt(10));
					System.out.println("Fourth Level: " + rs.getInt(11));					
				}
				rs.close();
				return 1;

			case 7:
				sql = "SELECT characterID, Character.name FROM `Character` WHERE (class=? AND level>0) OR (secondClass=? AND secondLevel>0) OR (thirdClass=? AND thirdLevel>0) OR (fourthClass=? AND fourthLevel>0) ";
				pstmt = conn.prepareStatement(sql);
				int id = Integer.parseInt(get("Enter class ID for which to count characters: "));
				pstmt.setLong(1,id);
				pstmt.setLong(2,id);
				pstmt.setLong(3,id);
				pstmt.setLong(4,id);
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("ID: " + rs.getInt(1) + "; Name: " + rs.getString(2));
				}
				rs.close();
				return 1;

			case 8:
				sql = "SELECT school, COUNT(*) FROM Spell NATURAL JOIN Effect INNER JOIN `Usage` ON Effect.parentUsage=usageID WHERE usageID=? GROUP BY school";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter Usage ID for which to count spells: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("School: " + rs.getString(1) + "; Number of Spells: " + rs.getInt(2));
				}
				rs.close();
				return 1;

			case 9:
				sql = "SELECT (level+secondLevel+thirdLevel+fourthLevel), COUNT(*) FROM `Character` WHERE (level+secondLevel+thirdLevel+fourthLevel)>=? GROUP BY (level+secondLevel+thirdLevel+fourthLevel) ORDER BY (level+secondLevel+thirdLevel+fourthLevel) ASC";
				pstmt = conn.prepareStatement(sql);
				pstmt.setLong(1,Integer.parseInt(get("Enter lowest level at which to count characters: ")));
				rs = pstmt.executeQuery();

				System.out.println();
				while (rs.next()) {
					System.out.println("Level: " + rs.getInt(1) + "; Number of Characters: " + rs.getInt(2));
				}
				rs.close();
				return 1;

			default:
				System.out.println("Invalid option.");
				return 0;


		}

	}

	public static void main(String[] args) {
		Connection conn = null;
		Statement stmt = null;
		try {
			// Registering JDBC driver
			Class.forName(JDBC_DRIVER);

			// Opening connection
			System.out.println("Connecting to 5e Spell database...");
			conn = DriverManager.getConnection(DB_URL,USER,PASS);

			stmt = conn.createStatement();
			String sql = "USE cpsc408_2295968";
			stmt.execute(sql);
			stmt.close();

			int choice = 0;

			while (choice != 5) {
				// Interface start
				System.out.println("\n----- LLOYD'S 5E SPELL DATABASE -----\n");
				System.out.println("Select an option:");
				System.out.println("\t1) Insert a record");
				System.out.println("\t2) Delete a record");
				System.out.println("\t3) Update a Character");
				System.out.println("\t4) Query table");
				System.out.println("\t5) Exit\n");
				System.out.print(">>> ");

				choice = Integer.parseInt(in.nextLine());

				switch (choice) {

					case 1:
						if (Insert(conn) != 0) {
							System.out.println("\nInsert successful!");
						} else {
							System.out.println("\nInsert failed.");
						}
						break;

					case 2:
						if (Delete(conn) != 0) {
							System.out.println("\nDelete successful!");
						} else {
							System.out.println("\nDelete failed.");
						}
						break;

					case 3:
						if (Update(conn) != 0) {
							System.out.println("\nUpdate successful!");
						} else {
							System.out.println("\nUpdate failed.");
						}
						break;

					case 4:
						if (Query(conn) != 0) {
							System.out.println("\nQuery successful!");
						} else {
							System.out.println("\nQuery returned no results.");
						}
						break;

					case 5:
						break;

					default:
						System.out.println("Invalid option");
						break;

				}

			}

		} catch(SQLException se){
			//Handle errors for JDBC
			se.printStackTrace();
		}catch(Exception e){
			//Handle errors for Class.forName
			e.printStackTrace();
		}finally{
		//finally block used to close resources
			try {
				if(stmt!=null)
			    	stmt.close();
			} catch(SQLException se2) {
			} try {
				if(conn!=null)
			    	conn.close();
			} catch(SQLException se) {
				se.printStackTrace();
			}
		}

		System.out.println("Goodbye, and happy adventuring!");

	}

}
