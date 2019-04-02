from .util import Util
from bs4 import BeautifulSoup

class GlobalStats:
    def __init__(self, html):
        self.current_players = None
        self.unranked_players = None
        self.duel_players = None
        self.doubles_players = None
        self.standard_players = None
        self.chaos_players = None
        self.private_players = None
        self.local_players = None
        self.exhibition_players = None
        self.training_players = None
        self.ranked_duel_players = None
        self.ranked_doubles_players = None
        self.ranked_solo_standard_players = None
        self.ranked_standard_players = None
        self.hoops_players = None
        self.rumble_players = None
        self.dropshot_players = None
        self.snowday_players = None

        # Load in html to populate data
        self._parse_html(html)

    def _parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.select("table.table > tbody td.playlist-value")
        for i in range(0, 16):
            data_id = data[i]['data-id']
            value = int(data[i].text.replace(',', ''))
            if data_id == 0:
                self.unranked_players = value
            elif data_id == 1:
                self.duel_players = value
            elif data_id == 2:
                self.doubles_players = value
            elif data_id == 3:
                self.standard_players = value
            elif data_id == 4:
                self.chaos_players = value
            elif data_id == 6:
                self.private_players = value
            elif data_id == 7:
                self.local_players = value
            elif data_id == 8:
                self.exhibition_players = value
            elif data_id == 9:
                self.training_players = value
            elif data_id == 10:
                self.ranked_duel_players = value
            elif data_id == 11:
                self.ranked_doubles_players = value
            elif data_id == 12:
                self.ranked_solo_standard_players = value
            elif data_id == 13:
                self.ranked_solo_standard_players = value
            elif data_id == 27:
                self.ranked_solo_standard_players = value
            elif data_id == 28:
                self.ranked_solo_standard_players = value
            elif data_id == 29:
                self.ranked_solo_standard_players = value
            elif data_id == 30:
                self.ranked_solo_standard_players = value


class PlayerCount:
    def __init__(self, current, peak):
        self.current = current
        self.peak = peak
