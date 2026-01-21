export type ShoppingItem = {
    id:number,
    user_name: string,
    item_name: string,
    quantity: number,
    created_at: string
}

export type CreateItem = {
    user_name: string,
    item_name: string,
    quantity: number,
    
}

type LoginSuccess = {
  ok: true;
  access_token: string;
};

type LoginFailure = {
  ok: false;
  message: string;
};

export type LoginResult = LoginFailure | LoginSuccess


type RegisterSuccess = {
  ok: true;
  access_token: string;
};

type RegisterFailure = {
  ok: false;
  message: string;
};

export type RegisterResult = RegisterFailure | RegisterSuccess