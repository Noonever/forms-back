import requests

generate_keysets_url = 'https://forms.yandex.ru/admin/gateway/root/form/generateKeyset'
download_form_xlxs_url = 'https://forms.yandex.ru/admin/proxy/form/exportKeyset' #?surveyId=64805434eb61463d0be9a076&keysetId=10251

def get_new_form_link(form_id: int) -> str:

    keyset_response = requests.post(
        headers={}, # TODO
        url=generate_keysets_url,
        data={} #  TODO
    ).json()
    keyset_id = keyset_response.get("") # TODO

    xlxs = requests.get(
        headers={}, # TODO
        url=download_form_xlxs_url,
        params={
            "surveyId": form_id,
            "keysetId": keyset_id
        }
    ).content
    # parse xlxs
    new_form_link = parse_xlxs(xlxs)
    return new_form_link


