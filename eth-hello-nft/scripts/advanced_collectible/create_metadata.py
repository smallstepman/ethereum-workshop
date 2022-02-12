#!/usr/bin/env python3
import json
from pathlib import Path

from brownie import AdvancedCollectible, network, config
import requests

from metadata.simple_metadata import metadata_template
from scripts.utils import get_breed

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectible = advanced_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectible} collectibles!")
    for token_id in range(number_of_advanced_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete file to override")
        else:
            print(f"Creating: {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = "adorable"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = None
            if config["upload_ipfs"]:
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as f:
                json.dump(collectible_metadata, f)
            if config["upload_ipfs"]:
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        resp = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        print(resp.text)
        ipfs_hash = resp.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
