import { mount } from '@vue/test-utils'
import { FontAwesomeIcon } from '../../../src/plugins/fa'
import { LangName } from '../../../src/ts/languages'
import Button from '../../../src/components/LangSelect/Button'

const defaults = {
  global: {
    components: {
      'fa': FontAwesomeIcon
    }
  }
}

describe('Language Selection / Button', () => {
  it('shows the correct language name passed from props', () => {
    const wrapper = mount(Button, {
      ...defaults,
      props: {
        name: LangName.RUS
      }
    })

    const btn = wrapper.find('button')
    expect(btn.text()).toStrictEqual(LangName.RUS)
  })

  describe('[EVENT] update-menu-visibility', () => {
    it('emits btn on click', async () => {
      const wrapper = mount(Button, defaults)
      const btn = wrapper.find('button')
      await btn.trigger('click')

      expect(wrapper.emitted('update-menu-visibility')).toBeTruthy()
    })

    it('returns opposite boolean state of showOptions', async () => {
      const wrapper = mount(Button, {
        ...defaults,
        props: {
          showOptions: false
        }
      })

      const btn = wrapper.find('button')

      await btn.trigger('click')
      expect(wrapper.emitted('update-menu-visibility')[0]).toEqual([true])

      await wrapper.setProps({
        showOptions: true
      })

      await btn.trigger('click')
      expect(wrapper.emitted('update-menu-visibility')[1]).toEqual([false])
    })
  })
})
