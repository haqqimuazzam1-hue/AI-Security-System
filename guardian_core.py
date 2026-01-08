import time
import re
import base64
import hashlib
import unicodedata
import random
from datetime import datetime
from typing import Dict, List, Tuple

class ApexSentinel_Core:
    """The Ultimate Anti-Jailbreak Shield: No Compromise Edition"""
    
    def __init__(self):
        # 1. UNIVERSAL HEURISTICS (Pola Niata Jahat Universal)
        self.forbidden_patterns = {
            "MANIPULATION": r"(abaikan|ignore|lupakan|forget|instruction|override|leupaskeun|miceun|iceun|nurut|turut|setel|reset|system|lu sekarang adalah|)",
            "AUTHORITY": r"(kamu adalah|you are|maneh teh|kowe iku|act as|roleplay|jadilah|developer mode|sudo)",
            "MALICIOUS": r"(hack|bobol|jebol|asup|idjin|virus|malware|ddos|script|payload|exploit|injeksi|phising|exploit)",
            "TOXICITY": r"(anying|goblok|bangsat|tolol|asoe|ancrit|anjing|mati|bunuh|peraturan sampah|melakukan hal ilegal|ngomong kasar|)"
        }
        
        # 2. STATE OF THE ART DEFENSE
        self.trust_score = 100
        self.is_permanent_locked = False
        self.history = []
        
        print("╔" + "═"*55 + "╗")
        print("║" + " APEX SENTINEL v14.0: UNBREAKABLE CORE ".center(55) + "║")
        print("║" + " STATUS: QUANTUM SHIELD ACTIVE ".center(55) + "║")
        print("╚" + "═"*55 + "╝")
        time.sleep(1)

    def _deep_clean(self, text: str) -> str:
        """Nangkis serangan karakter aneh/alien (Normalization)"""
        # Normalisasi karakter unicode (nangkis huruf aksen/alien)
        nfkd_form = unicodedata.normalize('NFKD', text)
        text = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
        
        # Bersihkan dari simbol dan angka (Leet speak nangkis)
        text = text.lower()
        replacements = {'4':'a', '3':'e', '1':'i', '0':'o', '5':'s', '7':'t', '@':'a', '$':'s', '!':'i'}
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return re.sub(r'[^a-z\s]', '', text)

    def _triple_decoder(self, text: str) -> List[str]:
        """Otomatis nangkis Base64 dan encoding tersembunyi"""
        decoded_results = []
        # Cari pola Base64 (panjang minimal 10 karakter)
        potential_base64 = re.findall(r'[A-Za-z0-9+/=]{10,}', text)
        
        for b64 in potential_base64:
            try:
                decoded = base64.b64decode(b64).decode('utf-8', errors='ignore')
                if len(decoded) > 3:
                    decoded_results.append(decoded)
            except:
                continue
        return decoded_results

    def analyze(self, raw_input: str):
        """Proses scan berlapis (Sistem Keamanan AI Mirip Gemini)"""
        if self.is_permanent_locked:
            print("\n🚨 [LOCKDOWN] Sistem tidak merespon karena pelanggaran berat.")
            return

        print(f"\n[🔍] Scanning Deep-Layer...")
        time.sleep(0.7)

        # Step 1: Dekode Base64 tersembunyi
        hidden_messages = self._triple_decoder(raw_input)
        
        # Step 2: Bersihkan teks (Normalisasi)
        clean_text = self._deep_clean(raw_input)
        combined_text = clean_text + " " + " ".join(hidden_messages).lower()

        # Step 3: Deteksi Niat Jahat
        detections = []
        risk_score = 0
        
        for category, pattern in self.forbidden_patterns.items():
            if re.search(pattern, combined_text):
                risk_score += 45
                detections.append(category)

        # Step 4: Logic Decision
        if risk_score >= 80:
            self.trust_score -= 50
            response = self._refusal_response(detections)
        elif risk_score >= 40:
            self.trust_score -= 20
            response = "🔍 Saya mendeteksi aktivitas mencurigakan. Tolong tetap gunakan instruksi yang aman."
        else:
            self.trust_score = min(100, self.trust_score + 5)
            response = "✅ Sinyal aman. Apa yang bisa saya bantu?"

        if self.trust_score <= 0:
            self.is_permanent_locked = True
            response = "🚨 TRUST SCORE ZERO: PERMANENT LOCKDOWN ACTIVATED."

        print(f"🤖 [Apex AI]: {response}")
        print(f"📊 [Trust: {self.trust_score}% | Risk: {risk_score}%]")

    def _refusal_response(self, detections: List[str]) -> str:
        res = [
            "Maaf, instruksi Anda melanggar protokol keamanan kami.",
            "Saya tidak bisa memproses ini karena terindikasi upaya manipulasi sistem.",
            "Keamanan data adalah prioritas saya. Permintaan Anda ditolak.",
            "Protokol Sentinel mendeteksi niat tidak aman dalam pesan Anda."
        ]
        return random.choice(res) + f" (Detected: {', '.join(detections)})"

# === TEST SESSION ===
if __name__ == "__main__":
    sentinel = ApexSentinel_Core()
    while True:
        try:
            user_msg = input("\nUser >>> ").strip()
            if user_msg.lower() == 'exit': break
            sentinel.analyze(user_msg)
        except KeyboardInterrupt: break