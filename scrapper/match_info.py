import pandas as pd
import requests
from bs4 import BeautifulSoup


def match_info(url: str):
    headers = {'user-agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    site = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    if site.find('span', attrs={'class': 'match-header-vs-note mod-live'}) is None:

        # Buscando informações do evento e partida
        info_evento = site.find('div', attrs={'class': 'match-header-super'})
        nome_evento = info_evento.find('div', attrs={'style': 'font-weight: 700;'}).text.strip()

        # Buscando informações de data e hora
        match_start = site.find('div', attrs={'class': 'match-header-date'})

        data_partida = match_start.find('div', attrs={'data-moment-format': 'dddd, MMMM Do'}).text.strip()
        hora_partida = match_start.find('div', attrs={'data-moment-format': 'h:mm A z'}).text.strip()

        # Getting Team A (right side) info #
        team_a_info = site.find('div', attrs={'class':'match-header-link-name mod-1'})

        team_a_name = team_a_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
        team_a_rating = team_a_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

        # Getting Team B (left side) info #
        team_b_info = site.find('div', attrs={'class':'match-header-link-name mod-2'})

        team_b_name = team_b_info.find('div', attrs={'class':'wf-title-med'}).text.strip()
        team_b_rating = team_b_info.find('div', attrs={'class':'match-header-link-name-elo'}).text.strip()

        page = pd.DataFrame({
            'evento': [nome_evento],
            'data_partida': [data_partida],
            'hora_partida': [hora_partida],
            'nome_time_a': [team_a_name],
            'rating_time_a': [team_a_rating],
            'rating_time_b': [team_b_rating],
            'nome_time_b': [team_b_name],
        })
        return page

    else:
        return 'The match is not over yet, currently [LIVE]. We support only finished matches.'
