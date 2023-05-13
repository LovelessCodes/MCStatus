# Minecraft Server Status Fetcher

## Description

This Python project is a fun and handy tool that allows you to fetch the status of a running Minecraft server using the routes provided by the [mc-router](https://github.com/itzg/mc-router) project. It leverages the Starlite framework to create a lightweight and efficient server status fetcher.

Whether you're a Minecraft enthusiast, a server administrator, or just curious about the status of a server, this project provides an easy way to retrieve valuable information about a Minecraft server. With a few simple steps, you can set up the server status fetcher and access various routes to retrieve real-time data.

## Installation

To get started, follow these instructions:

1. Clone this repository:

   ```
   git clone https://github.com/your-username/minecraft-server-status-fetcher.git
   ```

2. Change into the project directory:

   ```
   cd minecraft-server-status-fetcher
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:
     ```
     venv\Scripts\activate.bat
     ```
   - For Unix/macOS:
     ```
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set the environment variable(s)

    ```
    mv .env.example .env
    vim .env
    ```

6. Start the server:

   ```
   uvicorn main:app
   ```

7. By default, the server will run on `http://localhost:8000`.

## Usage

Once the server is up and running, you can access various routes to fetch the Minecraft server status and [mc-router](https://github.com/itzg/mc-router) routes:

- `/status`: Retrieves the general status of a Minecraft server.
- `/routes`: Retrieves, creates, modifies or deletes [mc-router](https://github.com/itzg/mc-router) routes.

The routes can be viewed at `http://localhost:8000/schema` and can be executed directly from there.

## Acknowledgments

This project was made possible by the [mc-router](https://github.com/itzg/mc-router) project, which provides the underlying routes for fetching the Minecraft server status. The Starlite framework enabled the development of a lightweight and efficient server status fetcher. Special thanks to the developers of both projects for their valuable contributions.

## Contributing

Contributions to this project are more than welcome! If you have any ideas, suggestions, bug reports, or feature requests, please submit them as issues or pull requests to the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Disclaimer

This project is an independent work and is not affiliated with or endorsed by Mojang Studios or the Minecraft brand. Minecraft is a registered trademark of Mojang Studios. Please refer to the [Minecraft EULA](https://account.mojang.com/documents/minecraft_eula) for information about the usage of Minecraft servers. Use this tool responsibly and in compliance with the applicable terms and conditions.