# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import asyncio

APP_NAME="google_search_agent"
USER_ID="user1234"
SESSION_ID="1234"

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-3-pro-preview",
    description="Agent to answer questions using Google Search.",
    instruction="""
You are a helpful assistant with access to Google Search.
If the user asks a question requiring current information, use the 'google_search' tool.
Always answer based on search results.
""",
    tools=[google_search]
)

async def setup_session_and_runner():
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner

async def call_agent_async(query):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(call_agent_async("what's the latest ai news?"))
