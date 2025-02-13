"use client";

import Image from "next/image";
import Link from "next/link";
import React from "react";
import Slider from "react-slick";

import brandImg1 from "../../public/images/brand/annecy.png";
import brandImg2 from "../../public/images/brand/cevec.png";
import brandImg3 from "../../public/images/brand/cred.png";
import brandImg4 from "../../public/images/brand/Logo_LISTIC-removebg-preview.png";
import brandImg5 from "../../public/images/brand/Logo_Polytech_Annecy_Chambery.svg-removebg-preview.png";
import brandImg6 from "../../public/images/brand/Logo_Sopra_Steria-removebg-preview.png";

const BrandList = () => {
  var settings = {
    centerMode: true,
    draggable: false,
    centerPadding: "150px",
    dots: false,
    arrows: false,
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 0,
    speed: 8000,
    pauseOnHover: true,
    cssEase: "linear",
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: "40px",
          slidesToShow: 4,
        },
      },
      {
        breakpoint: 992,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: "40px",
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: "40px",
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: "40px",
          slidesToShow: 1,
        },
      },
    ],
  };
  return (
    <>
      <Slider
        {...settings}
        className="brand-list brand-style-2 slider-brand slider-brand-activation"
      >
        <li className="slide-single-layout">
          <Link href="https://www.annecy.fr/">
            <Image
              src={brandImg1}
              width={500}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
        <li className="slide-single-layout">
          <Link href="https://cvec.etudiant.gouv.fr/">
            <Image
              src={brandImg2}
              width={132}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
        <li className="slide-single-layout">
          <Link href="https://www.credit-agricole.fr/">
            <Image
              src={brandImg3}
              width={300}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
        <li className="slide-single-layout">
          <Link href="https://www.univ-smb.fr/listic/">
            <Image
              src={brandImg4}
              width={125}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
        <li className="slide-single-layout">
          <Link href="https://www.univ-smb.fr/polytech/">
            <Image
              src={brandImg5}
              width={182}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
        <li className="slide-single-layout">
          <Link href="https://www.soprasteria.fr/">
            <Image
              src={brandImg6}
              width={120}
              height="auto"
              alt="Brand Image"
            />
          </Link>
        </li>
      </Slider>
    </>
  );
};

export default BrandList;
