import asyncio
from pathlib import Path
import edge_tts

TEXT = "You don't need a perfect plan. You need a consistent start."
VOICE = "en-US-GuyNeural"

async def main():
    out_dir = Path("outputs") / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "tts_test.mp3"

    communicate = edge_tts.Communicate(
        text=TEXT,
        voice=VOICE,
        rate="+0%",
        volume="+0%"
    )
    await communicate.save(str(out_path))
    print("Saved:", out_path)

if __name__ == "__main__":
    asyncio.run(main())
