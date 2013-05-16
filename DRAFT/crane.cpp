class Crane
{
	Point position;
	int rangeSight;
	int reach;
	int neighbourList[];

public:
	Crane()
	{
		position = new position(x, y);
	}

	void mainLoop()
	{
		while(statek wyslal zapytanie < x minut temu)
		{ 
			bool packageFound = examineSurroundings();
			if(packageFound)
			{

			}
			listen();
			movePackages();
		}
	}

	void receiveMessage(string message, int sender)
	{
		switch(message)
		{
			case "searchPackage":
				break;

			case "packageDelivered":
				break;

			case "movePackage":
				break;

			case "haveShipPath":
				break;

			case "moveArm":
				break;
		}
	}

	void sendMessage(string message, int sender)
	{
		switch(message)
		{
			case "passPackage":
				break;

			case "haveShipPath":
				break;

			case "seePackage":
				break;ho

			case "moveArm":
				break;
		}
	}
}