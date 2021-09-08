# -*- coding: utf-8 -*-
import base64
import requests
from .result import CorrectResult 
from bs4 import BeautifulSoup


# Go check out the __version__.py file for more information about this package ! This package has been translated
# using the translate() function of the package, as its creator is not a native English speaker.

class ReversoClient:

    def __init__(self):
        print("Reverso Client successfully created !")

    @staticmethod
    def is_supported(language):
        """
        This function let you know if the language you entered as source or target is supported by the Reverso api.
        :type language: str
        :rtype: bool
        """
        languages = [
            "de",
            "en",
            "ar",
            "ch",
            "es",
            "fr",
            "hb",
            "it",
            "jp",
            "nl",
            "pl",
            "pr",
            "ro",
            "ru",
            "tu"
        ]
        if language.lower() in languages:
            return True
        else:
            return False

    def language_to_api(self, language):
        """
        This function returns the three-letter abbreviation of the language, because the api uses three-letter
        abbreviation, and it is more common to use two-letter abbreviations for language names, so ... I created this
        function !
        :type language: str
        :rtype: str
        """
        languages = {
            "de": "ger",
            "en": "eng",
            "ar": "ara",
            "ch": "chi",
            "es": "spa",
            "fr": "fra",
            "hb": "heb",
            "it": "ita",
            "jp": "jpn",
            "nl": "dut",
            "pl": "pol",
            "pr": "por",
            "ro": "rum",
            "ru": "rus",
            "tu": "tur"
        }
        if self.is_supported(language):
            return languages.get(language)
        else:
            raise Exception(f"The language {language} is not supported.")

    def translate(self, source, target, text):
        """
        This function returns the translation of the given text using the api of allreverso, you can find the user
        interface at https://www.reverso.net/text_translation.aspx?lang=FR.
        :type source: str
        :type target:
        :type text: str
        :rtype: list
        """
        source = self.language_to_api(source)
        target = self.language_to_api(target)
        data = {
            "input": text,
            "from": source,
            "to": target,
            "format": "text",
            "options": {
                "origin": "reversodesktop",
                "sentenceSplitter": "true",
                "contextResults": "true",
                "languageDetection": "true"
            }
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "api.allreverso.net",
            "Origin": "https://www.reverso.net",
            "Referer": "https://www.reverso.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        }
        r = requests.post(url='https://api.reverso.net/translate/v1/translation',
                          json=data,
                          headers=headers)
        translation = r.json().get("translation")
        return translation

    def correct(self, language, text):
        """
        This function checks the spelling of the sentence given, but it works only in english and french.
        :type language: str
        :type text: str
        :rtype: str
        """
        if language == "fr" or language == "en":
            with requests.Session() as s:
                data = {'text': text}
                if language == "fr":
                    s.post("https://www.reverso.net/orthographe/correcteur-francais/ServerInterface.asmx/GetLgDetect", json=data)
                else:
                    s.post("https://www.reverso.net/orthographe/correcteur-anglais/ServerInterface.asmx/GetLgDetect", json=data)
                language = self.language_to_api(language)
                data = {
                    "language": language,
                    "text": text,
                    "autoReplace": "true",
                    "interfaceLanguage": "fr",
                    "locale": "Indifferent",
                    "origin": "interactive",
                    "generateSynonyms": "false",
                    "generateRecommendations": "false",
                    "getCorrectionDetails": "true"
                }
                headers = {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Content-Type": "application/json",
                    "Host": "orthographe.reverso.net",
                    "Origin": "https://www.reverso.net",
                    "Referer": "https://www.reverso.net/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
                }
                r = s.post(url="https://orthographe.reverso.net/api/v1/Spelling",
                                  json=data, headers=headers)
                return CorrectResult(**r.json())
        else:
            raise Exception(f"The language {language} is not supported by the spell checker api.")

    @staticmethod
    def synonymize(language, word):
        """
        A function to get a synonym for a given word. You can find the user interface at https://synonyms.reverso.net.
        :param word: The word to search
        :type word: str
        :param language: The language of the wanted synonym. It can be different of the source word's language.
        :type language: str
        :rtype: list
        """
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "orthographe.allreverso.net",
            "Origin": "https://www.reverso.net",
            "Referer": "https://www.reverso.net/",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        }
        if language != "tu" and language != "ch":
            r = requests.get(f"https://synonyms.reverso.net/synonyme/{language}/{word}", headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            synonyms_tags = soup.find_all("a", {"class": "synonym"})
            synonyms = []
            for synonym in synonyms_tags:
                synonyms.append(str(synonym.text))
                # synonyms.append(str(synonym.get("href")).replace(f"/synonyme/{language}/", ""))
            return synonyms
        else:
            raise Exception(f"The language {language} is not supported by the synonyms api.")

    @staticmethod
    def define(language, word):
        """
        A function to get a definition for a given word. You can find the user interface at
        https://dictionnaire.allreverso.net.
        :param language: The language of the source word.
        :type language: str
        :param word: The word to search.
        :type word: str
        :rtype: list
        /!\ I accept help with joy ! I have a little bit trouble with this function, because it returns all the spans,
        and I can't select only the definitions, so if you can and you want help me, open a pull request on github :
        https://github.com/PetitPotiron/python-allreverso/pulls
        """
        headers = {
            "Host": "woerterbuch.allreverso.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
        }
        supported_languages = [
            "de",
            "en",
            "es",
            "fr",

        ]

        language = language.lower()
        if language in supported_languages:
            if language == "de":
                r = requests.get("https://woerterbuch.reverso.net/deutsch-definition/" + word, headers=headers)
                soup = BeautifulSoup(r.text, "lxml")
                definitions = []
                definitions_tag = soup.find_all(
                    "span", {
                        "style": "color:#0;",
                        "direction": ""
                    }
                )
                for definition in definitions_tag:
                    if definition.text != " \xa0\xa0":
                        definitions.append(definition.text.replace(" \xa0\xa0", ""))
                return definitions
            elif language == "fr":
                r = requests.get("https://dictionnaire.reverso.net/francais-definition/" + word, headers=headers)
                soup = BeautifulSoup(r.text, "lxml")
                definitions = []
                definitions_tag = soup.find_all(
                    "span", {
                        "direction": "target"
                    }
                )
                for definition in definitions_tag:
                    if definition.text != " \xa0\xa0":
                        definitions.append(definition.text.replace("\xa0\xa0", ""))
                return definitions
            elif language == "en":
                r = requests.get("https://dictionary.reverso.net/english-definition/boat" + word, headers=headers)
                soup = BeautifulSoup(r.text, "lxml")
                definitions = []
                definitions_tag = soup.find_all(
                    "span", {
                        "direction": "target"
                    }
                )
                for definition in definitions_tag:
                    if definition.text != " \xa0\xa0":
                        definitions.append(definition.text.replace("\xa0\xa0", ""))
                return definitions
        else:
            raise Exception(f"The language {language} is not supported by the dictionnary api.")

    def speak_to_mp3(self, language, text):
        """
        A function wich creates a voice.mp3 file with the text read in the wanted language.
        :param language: The accent you want the voice to have.
        :type language: str
        :param text: The text to pronounce.
        :type text: str
        :rtype: str
        :return: "Successfully pronounced the text!"
        """
        text = base64.b64encode(text.encode("utf8")).decode("utf8")
        voice = ""
        if self.is_supported(language):
            if language == "de":
                voice = "Klaus22k"
            elif language == "en":
                voice = "Heather22k"
            elif language == "ar":
                voice = "Mehdi22k"
            elif language == "ch":
                voice = "Lulu22k"
            elif language == "es":
                voice = "Maria22k"
            elif language == "ch":
                voice = "Lulu22k"
            elif language == "fr":
                voice = "Bruno22k"
            elif language == "hb":
                voice = "he-IL-Asaf"
            elif language == "it":
                voice = "Chiara22k"
            elif language == "jp":
                voice = "Sakura22k"
            elif language == "it":
                voice = "Chiara22k"
            elif language == "nl":
                voice = "Femke22k"
            elif language == "pl":
                voice = "Monika22k"
            elif language == "pr":
                voice = "Celia22k"
            elif language == "ro":
                voice = "ro-RO-Andrei"
            elif language == "ru":
                voice = "Alyona22k"
            elif language == "tu":
                voice = "Ipek22k"
            r = requests.get(
                f"https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName={voice}?inputText={text}")
            with open("voice.mp3", "wb") as file:
                file.write(r.content)
                file.close()
            return "Successfully pronounced the text!"
        else:
            raise Exception(f"The language {language} is not supported by the voice api.")
