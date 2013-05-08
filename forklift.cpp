class Forklift
{
	Point position;
	int rangeSight;

public:
	Forklift()
	{
		position = new position(x, y);
	}

	void mainLoop()
	{
		while(statek wyslal zapytanie < x minut temu)
		{ 
			examineSurroundings();
			listen();
		}
	}

	void receiveMessage(string message, int sender)
	{
		switch(message)
		{
			case "searchPackage":
				break;

			case "getPackage":
				break;
		}
	}

	void sendMessage(string message, int sender)
	{
		switch(message)
		{
			case "passPackage":
				break;

			case "removePackage":
				break;
		}
	}
}