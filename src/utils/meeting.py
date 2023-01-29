from discord import Interaction


async def handle_meeting_button(i: Interaction):
    service = i.data["custom_id"]
    await i.response.send_message(f"{service}")
