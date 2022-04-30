import React from 'react';
import { Box, Flex, Heading, Stack } from '@chakra-ui/react';
import Head from 'next/head';

// import Image from 'next/image'; <- use this for images
// for NextJS, all static files, which includes images, goes in the `public/`
// For now put all images in `public/images/`

/*
--------------------
ChakraUI Vocabulary
--------------------
https://chakra-ui.com/docs/components/overview

<Box> == <div>
<FLex> == <div> with { display: flex; }
<Grid> == <div> with { display: grid; }

*also hovering over an element should give you info about it
*/

const Index = () => {
    return (
        <>
            <Head>
                <title>detox</title>
                <meta name="description" content="Toxicity analyzer" />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Flex justifyContent="center" alignItems="center" h="100vh">
                <Box>
                    <Stack spacing={6}>
                        <Heading as="h1" size="4xl">
                            This text should be getting smaller
                        </Heading>
                        <Heading as="h2" size="3xl">
                            If it is then that means
                        </Heading>
                        <Heading as="h2" size="2xl">
                            ChakraUI is successfully installed
                        </Heading>
                        <Heading as="h3" size="xl">
                            and working fine alongside NextJS and TypeScript
                        </Heading>
                        <Heading as="h3" size="lg">
                            Go team detox!!!
                        </Heading>
                    </Stack>
                </Box>
            </Flex>
        </>
    );
};

export default Index;
