import React from "react";

const ContactForm = () => {
  return (
    <>
      <form action="#" className="rbt-profile-row rbt-default-form row row--15">
        <div className="col-lg-6 col-md-6 col-sm-6 col-12">
          <div className="form-group">
            <label htmlFor="firstname1">Prénom</label>
            <input id="firstname1" type="text" placeholder="Fazlay" />
          </div>
        </div>
        <div className="col-lg-6 col-md-6 col-sm-6 col-12">
          <div className="form-group">
            <label htmlFor="lastname1">Nom</label>
            <input id="lastname1" type="text" placeholder="Elahi" />
          </div>
        </div>
        {/* <div className="col-lg-6 col-md-6 col-sm-6 col-12">
          <div className="form-group">
            <label htmlFor="username1">User Name</label>
            <input id="username1" type="text" placeholder="Rafi" />
          </div>
        </div> */}
        <div className="col-lg-6 col-md-6 col-sm-6 col-12">
          <div className="form-group">
            <label htmlFor="E-Mail">E-Mail</label>
            <input id="phonenumber1" type="tel" placeholder="+33 66-67-65-34" />
          </div>
        </div>
        <div className="col-12">
          <div className="form-group">
            <label htmlFor="bio1">Message</label>
            <textarea
              id="bio1"
              cols="20"
              rows="5"
              placeholder="Décrivez votre demande : comment pouvons-nous vous aider à promouvoir l’égalité dans l’ingénierie ?"
            ></textarea>
          </div>
        </div>
        <div className="col-12 mt--20">
          <div className="form-group mb--0">
            <a className="btn-default" href="#">
              Envoyer
            </a>
          </div>
        </div>
      </form>
    </>
  );
};

export default ContactForm;
