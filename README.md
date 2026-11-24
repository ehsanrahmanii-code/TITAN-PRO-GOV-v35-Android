# TITAN PRO GOV v3.5 PORTFOLIO — Android APK

TITAN PRO GOV **Portfolio Risk + Neon Studio + Governor + Core + Learning + Paper Trading** as a **self-contained Android APK**.

- Full modular Flask engine (numpy, pandas, flask, waitress) bundled via **Chaquopy**
- Data locked to **Internal Storage / ZZZ**
- Analysis-only crypto multi-timeframe dashboard + Studio + Portfolio risk panels
- **New neon icon** (bright cyan T glow)

## Build APK

1. Source is already in `app/src/main/python/` (or upload `TITAN_PRO_GOV_v3_5_PORTFOLIO.zip` to the root)
2. Go to **Actions** → **Build Titan PRO GOV v3.5 APK** → **Run workflow**
3. Wait ~15–25 min
4. Download the APK from **Artifacts** or the **Release**

## Install

1. Uninstall any previous Titan app
2. Install the APK
3. Grant **All files access** (Android 11+)
4. Wait 30–90 seconds for the engine to boot
5. Data & logs appear in `/storage/emulated/0/ZZZ/`

## Source

The original Python source is included under `app/src/main/python/`.  
The workflow can also unpack a ZIP from the repo root if needed.
