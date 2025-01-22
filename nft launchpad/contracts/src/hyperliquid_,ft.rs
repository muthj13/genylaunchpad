#![no_std]

use hyperliquid_std::prelude::*;

// Fictional attribute macros for the Hyperliquid environment
#[hyperliquid_contract]
pub mod hyperliquid_nft {
    use super::*;

    #[hyperliquid(storage)]
    pub struct HyperNFT {
        // Typically you'd store a mapping of token IDs to owners, but for brevity:
        pub owner: Address,
        pub token_uri: String,
    }

    impl HyperNFT {
        #[hyperliquid(constructor)]
        pub fn new(init_owner: Address, init_uri: String) -> Self {
            // Creates a simple NFT with a single token URI
            Self {
                owner: init_owner,
                token_uri: init_uri,
            }
        }

        #[hyperliquid(message)]
        pub fn get_owner(&self) -> Address {
            self.owner
        }

        #[hyperliquid(message)]
        pub fn get_token_uri(&self) -> String {
            self.token_uri.clone()
        }

        #[hyperliquid(message)]
        pub fn set_token_uri(&mut self, new_uri: String) {
            // Potentially restricted to owner only, but left open in this example
            self.token_uri = new_uri;
        }
    }
}
