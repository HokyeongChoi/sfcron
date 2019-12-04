import React, { useState, useEffect } from 'react';
import L from 'leaflet';

let map, marker, layer;

const LeafMap = ({ fes, res, full, invalidate, preventSwipe }) => {
    const [init, setInit] = useState(true);

    const Icon = L.icon({
        iconUrl: 'icon.png',
        iconSize: [20, 30]
    });

    let style;
    if (full) {
        style = <style jsx>{`
                            #map {
                                height: 100vh;
                                width: 100vw;
                                z-index: 1;
                            }
                            img {
                                width: 10vw;
                                height: 10vw;
                            }
                            .leaflet-control-zoom{
                                display: none;
                            }
                        `}</style>;
    } else {
        style = <style jsx>{`
                            #map {
                                width: 90vw;
                                height: 40vmax;
                                position: relative;
                                margin-left: 2.5vmin;
                            }
                            // .mapContainer {
                            //     position: fixed;
                            //     top: 22vmin;
                            //     left: 103.5vw;
                            //     overflow: hidden
                            // }
                        `}</style>;
    }

    useEffect(() => {
        if (full) {
            map = L.map('map').setView([37.564214, 127.001699], 12);
            for (let f of fes) {
                L.marker(
                    [f.y, f.x],
                ).bindPopup(
                    `${f.name}<br><img src='img/${f.id}.jpg'></img>`
                ).addTo(map);
            }
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
        } else if (invalidate) {
            // console.log("invalidate");
            if (!init) {
                map.remove();
            }
            map = L.map('map').setView([fes.y, fes.x], 15);
            marker = L.marker([fes.y, fes.x]).bindPopup(fes.name)
                .addTo(map).openPopup();
            for (let r of res) {
                L.marker(
                    [r.y, r.x],
                    { icon: Icon }
                ).bindPopup(
                    `${r.place_name}\n<a href=${r.place_url}>${r.place_url}</a>`
                ).addTo(map);
            }
            setInit(false);
            // L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            //     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            //     maxZoom: 18,
            //     id: 'mapbox.streets',
            //     accessToken: 'pk.eyJ1IjoiZG9sbGh5IiwiYSI6ImNrMnNraHRraDBpeGUzbXRqcm9hMTIxNnMifQ.s5z_Pkw604EFu087friCtQ'
            // }).addTo(map);
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            layer = L.layerGroup().addTo(map);
        }
    }, [fes, invalidate])



    return (
        <div className="mapContainer"
            onTouchStart={
                (preventSwipe)
                &&
                (e => {
                    preventSwipe(true);
                    function unregisterSwipe() {
                        preventSwipe(false);
                        window.removeEventListener('touchend', unregisterSwipe);
                    }
                    window.addEventListener('touchend', unregisterSwipe)
                })}
        >
            <div id='map'></div>

            {style}
        </div>
    );
}

export default LeafMap;