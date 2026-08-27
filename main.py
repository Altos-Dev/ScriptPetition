import json
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

URL = "https://www.mypetition.org/petition/social/pour-preserver-la-securite-et-la/282948"

with open("emails.json", "r", encoding="utf-8") as f:
    emails = json.load(f)["emails"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    for i, email in enumerate(emails, start=1):
        print(f"\n--- Test {i}/{len(emails)} : {email} ---")

        page = browser.new_page()

        try:
            page.goto(URL, wait_until="domcontentloaded")

            page.wait_for_timeout(200)

            accept = page.get_by_role("button", name="Tout accepter")
            try:
                accept.wait_for(state="visible", timeout=3000)
                accept.click()
            except PlaywrightTimeoutError:
                pass

            page.locator(
                'input[name="email"][type="email"]'
            ).wait_for()

            page.locator(
                'input[name="email"][type="email"]'
            ).fill(email)

            page.locator("#registration-no").check()

            page.locator("#block-btn-sign").click()

            print(f"✓ Test terminé : {email}")

            page.wait_for_timeout(200)

        except Exception as e:
            print(f"✗ Erreur : {e}")

        finally:
            page.close()

    print("\nTous les tests sont terminés.")
    input("Appuie sur Entrée pour fermer le navigateur...")

    browser.close()
