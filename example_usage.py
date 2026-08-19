from client import HighConvertingSocialAdCopyVariantSynthesizerClient

def main():
    client = HighConvertingSocialAdCopyVariantSynthesizerClient()
    res = client.synthesize_ad_variants("Autonomous Agent Fleet Infrastructure")
    print(f"Predicted CTR: {res['predicted_ctr_pct']}%")
    print(f"Hook Style: {res['hook_style']}")
    print("Variants Generated:", len(res["ad_variants"]))
    print("Variant 1:", res["ad_variants"][0])

if __name__ == "__main__":
    main()
