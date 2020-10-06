import { mount } from '@vue/test-utils'
import { LangCode, LangName } from '../../../src/ts/languages'
import Options from '../../../src/components/LangSelect/Options'

describe('Language Selection / Options Menu', () => {
  it('is not visible by default', () => {
    const wrapper = mount(Options, {
      props: {
        showOptions: false
      }
    })

    const menu = wrapper.find('div')
    expect(menu.exists()).toBeFalsy()
  })

  it('toggles menu visibility when showOptions is toggled', async () => {
    const wrapper = mount(Options, {
      props: {
        showOptions: true
      }
    })

    let menu = wrapper.find('div')

    expect(menu.exists()).toBeTruthy()

    await wrapper.setProps({
      showOptions: false
    })

    menu = wrapper.find('div')

    expect(menu.exists()).toBeFalsy()
  })

  it('emits update-lang when selecting language', async () => {
    const wrapper = mount(Options)
    await wrapper.vm.setLang(LangCode.RUSSIAN)
    expect(wrapper.emitted('update-lang')).toBeTruthy()
  })

  it('displays the correct active language', async () => {
    const wrapper = mount(Options, {
      props: {
        showOptions: true
      }
    })

    await wrapper.vm.setLang(LangCode.RUSSIAN)
    expect(wrapper.find('.active').text()).toStrictEqual(LangName.RUS)

    await wrapper.vm.setLang(LangCode.SPANISH)
    expect(wrapper.find('.active').text()).toStrictEqual(LangName.SPA)
  })
})
